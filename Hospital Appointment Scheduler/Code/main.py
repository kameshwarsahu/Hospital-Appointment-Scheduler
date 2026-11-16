from datetime import datetime

DOCTORS = ["Dr. Mehta", "Dr. Rao"]
appointments = {}   # {ID: {patient, doctor, date, time}}
counter = 100


def new_id():
    global counter
    counter += 1
    return "A" + str(counter)


def check_date(text):
    try:
        return datetime.strptime(text, "%d-%m-%Y").strftime("%d-%m-%Y")
    except ValueError:
        return None


def check_time(text):
    try:
        t = datetime.strptime(text, "%H:%M")
    except ValueError:
        return None
    minutes = t.hour * 60 + t.minute
    if 9 * 60 <= minutes <= 16 * 60 + 30 and t.minute % 30 == 0:
        return t.strftime("%H:%M")
    return None


def slot_taken(doctor, date, time, skip_id=None):
    for aid, a in appointments.items():
        if aid != skip_id and a["doctor"] == doctor and a["date"] == date and a["time"] == time:
            return True
    return False


def ask_date_time():
    date = check_date(input("Date (DD-MM-YYYY): ").strip())
    if date is None:
        print("Invalid date. Please enter the date as DD-MM-YYYY.")
        return None, None
    time = check_time(input("Time (HH:MM): ").strip())
    if time is None:
        print("Invalid time. Use HH:MM in 30-minute slots from 09:00 to 16:30.")
        return None, None
    return date, time


def book():
    patient = input("Patient: ").strip()
    doctor = input("Doctor: ").strip()
    match = [d for d in DOCTORS if d.lower() == doctor.lower()]
    if not patient or not match:
        print("Invalid patient or doctor. Doctors: Dr. Mehta, Dr. Rao.")
        return
    doctor = match[0]
    date, time = ask_date_time()
    if date is None:
        return
    if slot_taken(doctor, date, time):
        print(f"Slot unavailable: {doctor} already has an appointment on {date} at {time}.")
        return
    aid = new_id()
    appointments[aid] = {"patient": patient, "doctor": doctor, "date": date, "time": time}
    print(f"Appointment booked. ID: {aid} | {patient} | {doctor} | {date} {time}")


def view_all():
    for aid, a in appointments.items():
        print(f"{aid} | {a['patient']} | {a['doctor']} | {a['date']} {a['time']}")
    print("Total appointments:", len(appointments))


def reschedule():
    aid = input("Appointment ID: ").strip().upper()
    if aid not in appointments:
        print("Appointment ID not found.")
        return
    date, time = ask_date_time()
    if date is None:
        return
    if slot_taken(appointments[aid]["doctor"], date, time, skip_id=aid):
        print(f"Slot unavailable: {appointments[aid]['doctor']} already has an appointment on {date} at {time}.")
        return
    appointments[aid]["date"] = date
    appointments[aid]["time"] = time
    print(f"Appointment {aid} rescheduled to {date} {time}.")


def cancel():
    aid = input("Appointment ID: ").strip().upper()
    if aid in appointments:
        del appointments[aid]
        print(f"Appointment {aid} cancelled.")
    else:
        print("Appointment ID not found.")


def main():
    while True:
        print("\n--- Hospital Appointment Scheduler ---")
        print("1. Book\n2. View all\n3. Reschedule\n4. Cancel\n5. Exit")
        choice = input("Menu option: ").strip()
        if choice == "1":
            book()
        elif choice == "2":
            view_all()
        elif choice == "3":
            reschedule()
        elif choice == "4":
            cancel()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose 1-5.")


main()