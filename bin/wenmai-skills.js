#!/usr/bin/env node

'use strict';

const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');

const packageRoot = path.resolve(__dirname, '..');
const sourceRoot = path.join(packageRoot, 'skills');

function getAvailableSkills() {
  return fs
    .readdirSync(sourceRoot, { withFileTypes: true })
    .filter(
      (entry) =>
        entry.isDirectory() &&
        fs.existsSync(path.join(sourceRoot, entry.name, 'SKILL.md')),
    )
    .map((entry) => entry.name)
    .sort();
}

function getDefaultTarget(agent) {
  if (agent === 'codex') {
    const codexRoot = process.env.CODEX_HOME
      ? path.resolve(process.env.CODEX_HOME)
      : path.join(os.homedir(), '.codex');
    return path.join(codexRoot, 'skills');
  }

  if (agent !== 'wenmai-agent') {
    throw new Error(
      `Unsupported agent: ${agent}. Use "wenmai-agent" or "codex".`,
    );
  }

  if (process.env.WENMAI_SKILLS_DIR) {
    return path.resolve(process.env.WENMAI_SKILLS_DIR);
  }

  if (process.platform === 'darwin') {
    return path.join(
      os.homedir(),
      'Library',
      'Application Support',
      'Wenmai Agent',
      'wenmai-cli',
      'skills',
    );
  }

  if (process.platform === 'win32') {
    const appData =
      process.env.APPDATA || path.join(os.homedir(), 'AppData', 'Roaming');
    return path.join(appData, 'wenmaiAgent', 'wenmai-cli', 'skills');
  }

  throw new Error(
    'Automatic installation supports macOS and Windows. Use --dir <path> on this platform.',
  );
}

function printHelp() {
  console.log(`Wenmai Skills installer

Usage:
  npx @wenmai-ai/skills install [skill-name ...] [options]
  npx @wenmai-ai/skills list

Options:
  --agent <name> Install for wenmai-agent or codex (required without --dir)
  --dir <path>  Install into a custom skills directory
  --force       Replace skills that are already installed
  -h, --help    Show this help message

Examples:
  npx @wenmai-ai/skills install --agent wenmai-agent
  npx @wenmai-ai/skills install wenmai-sif-asin-keywords --agent wenmai-agent
  npx @wenmai-ai/skills install --agent codex
  npx @wenmai-ai/skills install --agent wenmai-agent --force`);
}

function parseInstallArgs(args) {
  const skillNames = [];
  let agent;
  let force = false;
  let target;

  for (let index = 0; index < args.length; index += 1) {
    const argument = args[index];

    if (argument === '--force') {
      force = true;
      continue;
    }

    if (argument === '--agent') {
      agent = args[index + 1];
      if (!agent) {
        throw new Error('--agent requires a name.');
      }
      index += 1;
      continue;
    }

    if (argument === '--dir') {
      target = args[index + 1];
      if (!target) {
        throw new Error('--dir requires a path.');
      }
      index += 1;
      continue;
    }

    if (argument === '--help' || argument === '-h') {
      printHelp();
      process.exit(0);
    }

    if (argument.startsWith('-')) {
      throw new Error(`Unknown option: ${argument}`);
    }

    skillNames.push(argument);
  }

  if (agent && agent !== 'wenmai-agent' && agent !== 'codex') {
    throw new Error(
      `Unsupported agent: ${agent}. Use "wenmai-agent" or "codex".`,
    );
  }

  if (!target && !agent) {
    throw new Error(
      '--agent is required. Use "--agent wenmai-agent", "--agent codex", or provide --dir <path>.',
    );
  }

  return {
    agent,
    force,
    skillNames: [...new Set(skillNames)],
    target: target ? path.resolve(target) : getDefaultTarget(agent),
  };
}

function install(args) {
  const availableSkills = getAvailableSkills();
  const availableSet = new Set(availableSkills);
  const { force, skillNames, target } = parseInstallArgs(args);
  const selectedSkills = skillNames.length > 0 ? skillNames : availableSkills;
  const unknownSkills = selectedSkills.filter((name) => !availableSet.has(name));

  if (unknownSkills.length > 0) {
    throw new Error(
      `Unknown skill${unknownSkills.length > 1 ? 's' : ''}: ${unknownSkills.join(', ')}. Run "npx @wenmai-ai/skills list" to see available skills.`,
    );
  }

  const existingSkills = selectedSkills.filter((name) =>
    fs.existsSync(path.join(target, name)),
  );

  if (existingSkills.length > 0 && !force) {
    throw new Error(
      `${existingSkills.length} skill${existingSkills.length > 1 ? 's are' : ' is'} already installed: ${existingSkills.join(', ')}. Run again with --force to replace ${existingSkills.length > 1 ? 'them' : 'it'}.`,
    );
  }

  fs.mkdirSync(target, { recursive: true });

  for (const skillName of selectedSkills) {
    const source = path.join(sourceRoot, skillName);
    const destination = path.join(target, skillName);

    if (force) {
      fs.rmSync(destination, { recursive: true, force: true });
    }

    fs.cpSync(source, destination, { recursive: true });
  }

  console.log(
    `Installed ${selectedSkills.length} skill${selectedSkills.length === 1 ? '' : 's'} to ${target}`,
  );
}

function main() {
  const [command = 'help', ...args] = process.argv.slice(2);

  if (command === 'install') {
    install(args);
    return;
  }

  if (command === 'list') {
    console.log(getAvailableSkills().join('\n'));
    return;
  }

  if (command === 'help' || command === '--help' || command === '-h') {
    printHelp();
    return;
  }

  throw new Error(`Unknown command: ${command}. Run with --help for usage.`);
}

try {
  main();
} catch (error) {
  console.error(`Error: ${error.message}`);
  process.exitCode = 1;
}
