#!/bin/bash

if [ -z "$DIR" ]
then 
  echo "Переменная DIR не задана. Поиск выполняется в текущей директории."
  DIR="."
fi

find_arg=$1
depth=$2

if [ -z "$find_arg" ]
then
  echo "Название файла не задано. Осуществляется поиск всех файлов в директории."
  find_arg="*"
fi

if [ -z "$depth" ]
then
  depth=1
fi

query=$(find $DIR -mindepth 1 -maxdepth $depth -iname "$find_arg")
echo "$query" > temp

if [ -z "$query" ]
then
  echo "Файлов не найдено."
else
  while read line
  do
    file "$line"
  done < temp
fi
rm -f temp
