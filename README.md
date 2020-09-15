# DataMade Code Challenge: Parserator

Hello! My name is Elliot Frank and this is my entry for the DataMade code challenge for the Developer 2 position (Sept 2020).

## How to clone

I mean I know you know how to do this. But:

```
git clone https://github.com/egfrank/code-challenge.git
```

And then my actual submission for the coding challenge is on the branch `parse_address`. You should simply be able to run:
```
git checkout parse_address
```
and git will create a local branch called `parse_address` that tracks the remote `parse_address` branch. 

## How to run

None of the instructions for local deployment have changed! Ie, make sure you're on the `parse_address` branch and then do
```
docker-compose build
```
to build the containers. 
To run the app, run:

```
docker-compose up
```
The app will log to the console, and you should be able to visit it at http://localhost:8000.

Part of the code challenge involved writing tests. To run them, run
```bash
docker-compose -f docker-compose.yml -f tests/docker-compose.yml run --rm app
```
