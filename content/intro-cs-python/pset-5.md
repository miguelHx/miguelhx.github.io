Title: Intro to CS: Problem Set 5
Date: 2026-01-22 11:15
Category: Intro to CS using Python
Tags: computer-science,python

Took about 2.22 hours, got tripped up a bit on `extract_end_bits` and `reveal_image` scaling parts.  Here is my code:  [https://github.com/miguelHx/intro-to-cs-mit-problem-sets/blob/main/1_ps5/ps5.py](https://github.com/miguelHx/intro-to-cs-mit-problem-sets/blob/main/1_ps5/ps5.py)

There was an easier way to do the extract end bits but I ended up doing a different way and did the update wrong where I did `px -= 2 ** i` instead of `px = px // 2` so it was thrown off for a bit (no pun intended). So I lost some time there.

For reveal image I guessed how they wanted to scale it, for the b/w scale I just moved the bit up to the msb, I could kinda see the hidden image but it was very faint. Then I saw the solution image and that led me right away to making pixel white if LSB was 1, black otherwise and the image came out properly and passed the test For colored reveal image, I scaled by just taking the 3 lsbs, and moving them up to the next 3 bits places.

The image came out faint and so it didn't pass the test. So I decided to move the least 3 bits to the most 3 bits, and zeroing out the lsbs, keeping everything else. The hidden image came out clear, but didn't pass the test. Tried out zeroing out the bits in between and the hidden image extraction still worked even though the last test is failing.

I could reverse engineer using the solution but I decided it wasn't worth the extra effort. Going to leave my solution as-is. Also wasted several minutes trying to calculate the width/height of an image, when I found out that the size property comes with the image lol. D'oh.

I’m a bit disappointed that they didn’t tell you How they wanted us to scale the image using the least significant bits.  They just said scale it, which left room for ambiguity.

