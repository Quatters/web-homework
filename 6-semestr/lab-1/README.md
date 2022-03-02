```bash
tail -n 40 file1 > file2 && head -n 10 file2 > file3 \
&& cat file2 | grep коко > temp && sed -i 's/коко/куку/g' \
temp && head -n 3 temp >> file3 && rm -f temp && sort \
file3 | uniq -c && sort -u file3 -o file3
```

Результат:
![Alt text](result.jpg?raw=true 'Результат')
