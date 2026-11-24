# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/itzalisha99/postmortem-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/itzalisha99/postmortem-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

A make.fun entry for **The Postmortem That Made Us Laugh**: one short account
(two sentences, 143 characters) of the silliest time an AI coding agent
misunderstood what it was asked to do.

## The entry

> I asked it to log every payment attempt. It put the log line after the
> payment call, so the only payments with no log are the ones that failed.

## Run

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt`. Standard library only, deterministic.
