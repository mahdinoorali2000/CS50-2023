-- Keep a log of any SQL queries you execute as you solve the mystery.
-- I wanted to check the description
SELECT description from crime_scene_reports
WHERE year = 2021
    AND month =7
    AND day = 28
    AND street = "Humphrey Street";

--I want to read the text of the reports that only mention the bakery to find new clues
SELECT name , transcript FROM interviews
WHERE year = 2021
    AND month = 7
    AND day = 28
    and transcript LIKE "%baker%";

--People out of the bakery
SELECT name, bakery_security_logs.hour, bakery_security_logs.minute
FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE bakery_security_logs.year = 2021
    AND bakery_security_logs.month = 7
    AND bakery_security_logs.day = 28
    AND bakery_security_logs.hour = 10
    AND bakery_security_logs.minute > 15
    AND bakery_security_logs.minute < 40;

--Who made a transaction at Leggett Street ATM that day?
SELECT name FROM people
    JOIN bank_accounts ON people.id = bank_accounts.person_id
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
WHERE year = 2021
    AND month = 7
    AND day = 28
    AND atm_location = "Leggett Street";

--Check the flights and people as well as the destination city
SELECT flights.id, name, city, flights.hour, flights.minute FROM people
    JOIN passengers ON passengers.passport_number = people.passport_number
    JOIN flights ON passengers.flight_id = flights.id
    join airports ON flights.destination_airport_id = airports.id
WHERE flights.year = 2021
    AND flights.month = 7
    AND flights.day = 29
    AND flights.origin_airport_id IN (SELECT origin_airport_id FROM flights JOIN airports ON flights.origin_airport_id = airports.id WHERE airports.city = "Fiftyville")
ORDER BY flights.hour;

--I want to find his accomplice, the person who bought the ticket
SELECT name, duration FROM people JOIN phone_calls ON people.phone_number = phone_calls.caller
WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration <=60;

SELECT name, duration FROM people JOIN phone_calls ON people.phone_number = phone_calls.receiver
WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration <=60;