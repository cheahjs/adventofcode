#!/usr/bin/env bash

DAY=$1

touch "day${DAY}-1.txt"
touch "day${DAY}-test.txt"
echo "#!/usr/bin/env python3" >"day${DAY}-1.py"
