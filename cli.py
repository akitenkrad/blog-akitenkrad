import shutil
from datetime import datetime
from pathlib import Path

import click


@click.group()
def cli():
    pass


@cli.command()
def new_post():
    meta_text = f"""---
draft: false
title: "TITLE"
date: {datetime.now().strftime('%Y-%m-%d')}
author: "akitenkrad"
description: "DESCRIPTION"
tags: [""]
menu:
  sidebar:
    name: {datetime.now().strftime('%Y.%m.%d')}
    identifier: {datetime.now().strftime('%Y%m%d')}
    parent: papers
    weight: 10
math: true
---

## Citation

## Abstract

## What's New

## Dataset

## Model Description

## Results

"""

    new_post_path = Path(f"src/content/posts/{datetime.now().strftime('%Y%m%d%H%M%S')}/index.md")
    new_post_path.parent.mkdir(parents=True, exist_ok=True)
    with open(new_post_path, mode="wt", encoding="utf-8") as wf:
        wf.write(meta_text)

    shutil.copy("src/resources/assets/images/hero.jpg", str(new_post_path.parent / "hero.jpg"))

    print(f"New Post -> {str(new_post_path.absolute())}")


if __name__ == "__main__":
    cli()
