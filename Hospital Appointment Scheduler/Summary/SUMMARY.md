# Hospital Appointment Scheduler
**PS No. 81 – Rungta International Skills University**

## Project Overview

The Hospital Appointment Scheduler is a console-based Python program built for a clinic receptionist. It allows the receptionist to book, view, reschedule and cancel patient appointments from a simple menu. All appointments are stored in a dictionary with an auto-generated ID (A101, A102, and so on). Every date and time is validated using the `datetime` module, and the program makes sure a doctor is never booked twice at the same time.

## Objectives

- Build a menu-driven program that repeats until the user chooses Exit.
- Store appointments in a dictionary using an auto-generated ID as the key.
- Validate dates (DD-MM-YYYY) and times (HH:MM) using the `datetime` module.
- Accept only 30-minute slots from 09:00 to 16:30.
- Prevent two appointments for the same doctor at the same date and time.

## Key Results

- All 4 test cases passed (normal, boundary, invalid and different valid scenario)
- Slots: 30 minutes, 09:00 to 16:30
- Doctors: Dr. Mehta, Dr. Rao
- First appointment ID generated: A101

## Main Points

1. A dictionary stores all appointments, with the appointment ID as the key, so any appointment can be found instantly.
2. IDs are generated automatically, so the receptionist never has to create or remember them.
3. The `datetime` module checks both date and time, so impossible dates such as 31-11-2026 are rejected.
4. Time slots are limited to 30-minute gaps between 09:00 and 16:30, so the last valid slot is 16:30.
5. A clash check stops one doctor from having two appointments at the same date and time.
6. The program covers full CRUD: Create (Book), Read (View all), Update (Reschedule) and Delete (Cancel).
7. Functions are used for every task (validate, book, reschedule, cancel), which keeps the code clean and easy to extend.
8. Clear error messages tell the user exactly what went wrong, such as "Slot unavailable" or "Invalid date".

## Difficulties Faced During Development

1. **Test cases in one session:** The appointment ID counter resets every time the program is restarted, so all test cases had to be run in one session to get the correct IDs (A101, A102).
2. **Time validation:** A wrongly typed time (for example 06:30 instead of 16:30) was correctly rejected with an "Invalid time" message, because only 30-minute slots from 09:00 to 16:30 are allowed.
3. **Matching the expected output:** The messages had to match the given test cases exactly, so each print statement was checked carefully.

## Conclusion

The program handles all appointment operations correctly and rejects invalid dates, invalid times and double-booked slots. It meets all the bare minimum requirements and passes all four test cases.

---

*PS No. 81 – Rungta International Skills University*