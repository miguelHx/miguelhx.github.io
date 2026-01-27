Title: Intro to CS: Problem Set 5
Date: 2026-01-22 11:15
Category: Intro to CS using Python
Tags: computer-science,python

It was a little harder than expected. Took about 2.22 hours, got tripped up a bit on `extract_end_bits` and `reveal_image` scaling parts.  Here is my code:  [https://github.com/miguelHx/intro-to-cs-mit-problem-sets/blob/main/1_ps5/ps5.py](https://github.com/miguelHx/intro-to-cs-mit-problem-sets/blob/main/1_ps5/ps5.py)

There was an easier way to do the extract end bits on google but I ended up doing it my way and did the update wrong where i did `px -= 2 ** i` instead of `px = px // 2` so it was thrown off for a bit. So I lost some time there. For reveal image I guessed how they wanted to scale it, for the b/w scale i just moved the bit up to the msb, I could kinda see the hidden image but it was very faint. Then i saw the solution image and that led me right away to making pixel white if LSB was 1, black otherwise and the image came out properly and passed the test For colored reveal image, I scaled by just taking the 3 lsbs, and moving them up to the next 3 bits places. 

The image came out faint and so it didn't pass the test. So I decided to move the least 3 bits to the most 3 bits, and zeroing out the lsbs, keeping everything else. The hidden image came out clear, but didn't pass the test. Tried out zeroing out the bits in between and still didn't work Even though the last test is failing, not going to waste more time on the exact way they wanted us to scale it, going to leave my solution as-is. Also wasted several minutes trying to calculate the width/height of an image, when I found out that the size property comes with the image lol.

I’m a bit disappointed that they didn’t tell you How they wanted us to scale the image using the least significant bits.  They just said scale it.  So I did, using my own method, which yielded the proper hidden image, but off by some factor because the test doesn’t pass.

