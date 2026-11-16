# Hospital Appointment Scheduler
**PS No. 81 – Rungta International Skills University**

## About the Project

The Hospital Appointment Scheduler is a menu-driven Python console program built for a clinic receptionist. It lets the receptionist book, view, reschedule and cancel patient appointments without any paperwork. All appointments are stored in a dictionary with an auto-generated ID (A101, A102, and so on), and every date and time entered is checked using Python's `datetime` module, so wrong entries are rejected immediately.

## Key Features

- **Book appointments:** Takes the patient name, doctor, date and time, then generates a unique appointment ID.
- **View all appointments:** Lists every appointment with its ID, patient, doctor, date and time, along with the total count.
- **Reschedule:** Changes the date and time of an existing appointment using its ID.
- **Cancel:** Removes an appointment using its ID.
- **Input validation:** Dates must be in DD-MM-YYYY format and times in HH:MM format, and invalid values show a clear error message.
- **Clash prevention:** One doctor cannot have two appointments at the same date and time.
- **Repeating menu:** The menu keeps running until the user chooses Exit.

## Technologies Used

- **Python 3:** Main programming language
- **Dictionaries:** Store appointments with the ID as the key
- **Datetime module:** Validates dates and times
- **Functions:** Keep the code organised, with one function per task

## Project Structure

```
Hospital_Appointment_Scheduler/
├── Summary/
│   └── SUMMARY.md
├── README/
│   └── README.md
├── Code/
│   └── main.py
└── Screenshots/
    ├── test1.png
    ├── test2.png
    ├── test3a.png
    ├── test3b.png
    ├── test4a.png
    ├── test4b.png
    └── test4c.png
```

## How to Use

1. Install Python 3 on your computer.
2. Open the `Code` folder.
3. Run the program:
   ```
   python main.py
   ```

## Menu Options

| Option | Name | What It Does |
|--------|------|--------------|
| 1 | Book | Creates a new appointment and shows its ID |
| 2 | View all | Shows all appointments and the total count |
| 3 | Reschedule | Updates the date and time of an appointment |
| 4 | Cancel | Deletes an appointment |
| 5 | Exit | Closes the program |

## Rules

- **Slots:** 30 minutes each, from 09:00 to 16:30
- **Date format:** DD-MM-YYYY
- **Time format:** HH:MM (24-hour)
- **Doctors available:** Dr. Mehta, Dr. Rao
- **No double booking:** One doctor cannot have two appointments at the same time

## Main Points

1. The program covers full CRUD operations: Create (Book), Read (View all), Update (Reschedule) and Delete (Cancel).
2. A dictionary gives fast lookup, because each appointment can be found directly by its ID.
3. Appointment IDs are generated automatically, so the receptionist never has to type or remember a new ID.
4. The `datetime` module rejects impossible dates such as 31-11-2026, which prevents wrong data from being saved.
5. The clash check keeps each doctor's schedule free of overlapping appointments.
6. Splitting the code into functions makes it easier to read, test and extend.
7. The program was tested with four test cases: normal input, boundary input, invalid input and a different valid scenario (reschedule, cancel and view).

## Test Cases Covered

| Test | Scenario | Result |
|------|----------|--------|
| 1 | Normal booking (10:00) | Appointment A101 booked |
| 2 | Boundary booking (last slot, 16:30) | Appointment A102 booked |
| 3 | Invalid input (already booked slot, invalid date) | Clear error messages shown |
| 4 | Reschedule, cancel and view all | Changes applied, total appointments: 1 |

## Limitations

- Data is stored in memory only, so all appointments are lost when the program closes.
- Only two doctors are supported, and the list is fixed in the code.

## Future Improvements

- Save appointments to a file or database so they are not lost.
- Add more doctors and departments.
- Add search by patient name or by date.
- Build a graphical interface or a web version.

---

*PS No. 81 – Rungta International Skills University*