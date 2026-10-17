for i in 1 2 3; do python3 condense.py part1/05-computer && [ $(wc -m < out5/part1/05-computer.md) -gt 4000 ] && break; done
echo C5DONE
