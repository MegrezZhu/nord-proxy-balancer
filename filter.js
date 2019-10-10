#!/usr/bin/env node

const fs = require('fs');
const assert = require('assert');
const yargs = require('yargs');

const parseArgs = () => {
    const args = yargs.argv;

    const type = args.type.toString().toLowerCase();
    assert(type, 'Missing type');

    const country = args.country || 'United States';

    const port = Number(args.port);
    assert(port, 'Missing port');

    const loadThreshold = Number(args.load) || 70;
    const limit = Number(args.limit) || 50;

    return {
        type,
        port,
        loadThreshold,
        limit,
        country
    }
}

const serverFilter = (type) => (o) => {
    switch (type) {
        case 'p2p':
            return o.features['socks'] && o.categories.some(oo => oo.name === 'P2P');
        case 'http':
            return o.features['proxy'];
        default:
            throw new Error(`Unknown type ${type}`);
    }
}

const sample = (arr, n) => arr
    .map(a => [a, Math.random()])
    .sort((a, b) => a[1] < b[1] ? -1 : 1)
    .slice(0, n)
    .map(a => a[0]);

const data = JSON.parse(fs.readFileSync('/dev/stdin').toString());
const args = parseArgs();

const servers = data
    .filter(o => o.country === args.country)
    .filter(serverFilter(args.type))
    .filter(o => o.load <= args.loadThreshold);

const samples = sample(servers, args.limit);
const configStr = samples.map(s => `server ${s.domain}:${args.port} max_fails=2 fail_timeout=30s;`).join('\n');

process.stdout.write(configStr);
