# List_Filtering_in_Python

[![License: AGPL](https://img.shields.io/badge/License-AGPL-blue.svg)](https://github.com/gotreasa/list_filtering_in_python/blob/main/LICENSE)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_list_filtering_in_python&metric=alert_status)](https://sonarcloud.io/dashboard?id=gotreasa_list_filtering_in_python)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_list_filtering_in_python&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=gotreasa_list_filtering_in_python)
[![Build Status](https://github.com/gotreasa/list_filtering_in_python/actions/workflows/cicd.yml/badge.svg)](https://github.com/gotreasa/list_filtering_in_python/actions/workflows/cicd.yml)
[![Can I Deploy main to test](https://gotreasa.pactflow.io/pacticipants/list_filtering_in_python_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)](https://gotreasa.pactflow.io/hal-browser/browser.html#https://gotreasa.pactflow.io/pacticipants/list_filtering_in_python_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)

Welcome to the Python Template created via a cookiecutter recipe. The project template is designed for a development via a `Double Loop approach` (BDD-TDD) using pytest and several other pytest libs.

## Description

In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

### Example

```python
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
```
