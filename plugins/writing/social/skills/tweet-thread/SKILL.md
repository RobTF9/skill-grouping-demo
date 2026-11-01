---
name: tweet-thread
description: Turn an article into a thread of short posts.
allowed-tools:
  - Bash
  - WebFetch
---

# Thread

Split the article into posts of 280 characters or fewer. Number each post as 1/n.

## Steps

1. Read the article and find the one claim that matters most.
2. Write the first post as a hook: the claim, in plain words.
3. Give each post after it one supporting point.
4. End with a post that links to the article.
5. Check each post with scripts/count_chars.py.

## Rules

- Never more than 8 posts.
- No hashtags in the first post. See [hashtags](references/hashtags.md).
- One emoji at most, and only at the end of a post.
- Quote the author by name when you use their words.

## Examples

See [a launch thread](references/examples/launch.md).
