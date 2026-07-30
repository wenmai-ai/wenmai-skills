'use strict';

const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { spawnSync } = require('node:child_process');
const test = require('node:test');

const cli = path.resolve(__dirname, '..', 'bin', 'wenmai-skills.js');

function runCli(args, env = {}) {
  return spawnSync(process.execPath, [cli, ...args], {
    encoding: 'utf8',
    env: { ...process.env, ...env },
  });
}

test('lists all packaged skills', () => {
  const result = runCli(['list']);
  const skills = result.stdout.trim().split('\n');

  assert.equal(result.status, 0, result.stderr);
  assert.equal(skills.length, 69);
  assert.ok(skills.includes('wenmai-sif-asin-keywords'));
});

test('requires an explicit agent without a custom directory', () => {
  const result = runCli(['install', 'wenmai-sif-asin-keywords']);

  assert.notEqual(result.status, 0);
  assert.match(result.stderr, /--agent is required/);
});

test('installs one skill and protects existing installations', (context) => {
  const temporaryRoot = fs.mkdtempSync(
    path.join(os.tmpdir(), 'wenmai-skills-test-'),
  );
  context.after(() => fs.rmSync(temporaryRoot, { recursive: true, force: true }));

  const target = path.join(temporaryRoot, 'skills');
  const installArgs = [
    'install',
    'wenmai-sif-asin-keywords',
    '--dir',
    target,
  ];
  const firstInstall = runCli(installArgs);

  assert.equal(firstInstall.status, 0, firstInstall.stderr);
  assert.ok(
    fs.existsSync(path.join(target, 'wenmai-sif-asin-keywords', 'SKILL.md')),
  );

  const protectedInstall = runCli(installArgs);
  assert.notEqual(protectedInstall.status, 0);
  assert.match(protectedInstall.stderr, /already installed/);

  const forcedInstall = runCli([...installArgs, '--force']);
  assert.equal(forcedInstall.status, 0, forcedInstall.stderr);
});

test('installs all skills', (context) => {
  const temporaryRoot = fs.mkdtempSync(
    path.join(os.tmpdir(), 'wenmai-skills-test-'),
  );
  context.after(() => fs.rmSync(temporaryRoot, { recursive: true, force: true }));

  const target = path.join(temporaryRoot, 'skills');
  const result = runCli(['install', '--dir', target]);
  const installedSkills = fs
    .readdirSync(target, { withFileTypes: true })
    .filter((entry) => entry.isDirectory());

  assert.equal(result.status, 0, result.stderr);
  assert.equal(installedSkills.length, 69);
});

test('installs into the Codex user directory', (context) => {
  const temporaryRoot = fs.mkdtempSync(
    path.join(os.tmpdir(), 'wenmai-skills-test-'),
  );
  context.after(() => fs.rmSync(temporaryRoot, { recursive: true, force: true }));

  const result = runCli(
    ['install', 'wenmai-sif-asin-keywords', '--agent', 'codex'],
    { CODEX_HOME: temporaryRoot },
  );

  assert.equal(result.status, 0, result.stderr);
  assert.ok(
    fs.existsSync(
      path.join(temporaryRoot, 'skills', 'wenmai-sif-asin-keywords', 'SKILL.md'),
    ),
  );
});

test('installs into the Wenmai Agent directory', (context) => {
  const temporaryRoot = fs.mkdtempSync(
    path.join(os.tmpdir(), 'wenmai-skills-test-'),
  );
  context.after(() => fs.rmSync(temporaryRoot, { recursive: true, force: true }));

  const result = runCli(
    ['install', 'wenmai-sif-asin-keywords', '--agent', 'wenmai-agent'],
    { WENMAI_SKILLS_DIR: temporaryRoot },
  );

  assert.equal(result.status, 0, result.stderr);
  assert.ok(
    fs.existsSync(
      path.join(temporaryRoot, 'wenmai-sif-asin-keywords', 'SKILL.md'),
    ),
  );
});
