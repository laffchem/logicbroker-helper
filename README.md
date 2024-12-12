# Logicbroker Helper

If you have python installed you're good to go.

## Installation Instructions

**In the terminal, ensure you're in the directory and then this will explain how to install the program**

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

### How to use

Paste the agreement ids, or the calypso links inside the input-values.txt (I like using agreementIds better...)

Run the main.py file in the src directory. You will be greeted with a list of options.

- `hold` and `release` (options 1 and 2) are not used anymore as CS should be able to accomplish these but I left them in just in case.
- `bb_release` is Best Buy release for the Risk & AppSupport channels.
- `repeat_customer_release` is for the hourly customer release email reports.

Run the program and select the values.

Calypso links
ID Values

Select if you need a hold or release query.

**Then after the program runs, the query is generated to output.txt.**

_Underneath the query to hold or release is the SELECT query so you can check if there are any that were already submitted_

You can paste that into mysql and make this a little more simple.
