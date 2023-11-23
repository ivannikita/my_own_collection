# Ansible collection: my own test collection
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)  

## Description

Тестовая коллекция для создания файла с данными на удаленном сервере


## Requirements

- Ansible >= 2.7

## Role Variables

Все параметры расположены в  [defaults/main.yml](defaults/main.yml) и могут быть переопределены.

| Имя           | Исходное значение | Описание                        |
| -------------- | ------------- | -----------------------------------|
| `path` | /tm/file.create | Путь для размещения файла  |
| `content` | test start | данные которые нужно поместить в файл  |
