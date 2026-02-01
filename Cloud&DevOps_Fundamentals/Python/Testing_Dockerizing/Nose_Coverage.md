# Index

- [[#Nose + Coverage]]
	- [[#Install Nose and Coverage]]
	- [[#Run tests]]
	- [[#Run tests and coverage calculation]]
	- [[#Check coverage]]
	- [[#Generate coverage report (cover/index.html)]]
	- [[#Testing process]]
- [[#Next Notes]]
# Nose + Coverage

## Install Nose and Coverage

```shell
$ pip install nose
$ pip install coverage
```

## Run tests

```shell
$ nosetests
```

## Run tests and coverage calculation

```shell
$ nosetests --with-coverage --cover-package=handlers/ --cover-erase
```

## Check coverage

```shell
$ nosetests --with-coverage --cover-package=handlers/ --cover-erase --cover-min-percentage=90
```

## Generate coverage report (cover/index.html)

```shell
$ nosetests --with-coverage --cover-package=handlers/ --cover-erase --cover-html
```

## Testing process

![[testing.gif]]

# Next Notes

[[Tox]]