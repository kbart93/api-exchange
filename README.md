# Currency Exchange App

## Introduction

Currency Exchange App is a small Python project that serves as an electronic currency exchange platform. It utilizes basic Python functionalities such as functions, while and for loops, and the requests library to interact with the API provided by the National Bank of Poland. The app allows users to fetch current exchange rates for various world currencies and automatically convert currencies to Polish Zloty (PLN).

## Technologies

- Python
- library: requests 2.82.2

## How to Run

### Setup

Before you begin, ensure you have the following installed:
- Python 3.x
- requests library version 2.82.2
### Instructions

1. Clone the repository to your local machine.
```sh
git clone https://github.com/kbart93/api-exchange
```
2. Navigate to the project directory.
```sh
cd currency-exchange-app
```
3. Run the Python script.
```sh
python currency_exchange.py
```

The app will prompt you to enter the currency code you want to convert, the amount, and the target currency. It will then fetch the latest exchange rates from the National Bank of Poland API and display the converted amount in PLN.