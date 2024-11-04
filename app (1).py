from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def create_connection(): 
    """ Create a database connection to the MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345',
            database='medical'
        )
        if conn.is_connected():
            print("Connection successful")
    except Error as e:
        print(f"Error: {e}")
    return conn

def execute_query(conn, query, data=None):
    """ Execute a single query """
    cursor = conn.cursor()
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        conn.commit()
        print("Query successful")
    except Error as e:
        print(f"Error: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_patient', methods=['POST'])
def add_patients():
    patient_id = request.form['patientID']
    patient_name = request.form['patientName']
    patient_age = request.form['patientAge']
    patient_gender = request.form['patientGender']
    patient_medical_history = request.form['patientMedicalHistory']

    query = """
    INSERT INTO patients (patientID,patientName, patientAge, patientGender, patientMedicalHistory)
    VALUES (%s,%s, %s, %s, %s)
    """
    data = (patient_id,patient_name, patient_age, patient_gender, patient_medical_history)
    
    conn = create_connection()
    execute_query(conn, query, data)
    conn.close()

    return redirect(url_for('index'))

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    doctor_id = request.form['doctorID']
    doctor_name = request.form['doctorName']
    doctor_specialization = request.form['doctorSpecialization']

    query = """
    INSERT INTO doctors (doctorID,doctorName, doctorSpecialization)
    VALUES (%s,%s, %s)
    """
    data = (doctor_id,doctor_name, doctor_specialization)
    
    conn = create_connection()
    execute_query(conn, query, data)
    conn.close()

    return redirect(url_for('index'))

@app.route('/add_appointment', methods=['POST'])
def add_appointment():
    appointment_id= request.form['appointmentID']
    appointment_date = request.form['appointmentDate']
    appointment_time = request.form['appointmentTime']
    patient_id = request.form['patientID']
    doctor_id = request.form['doctorID']

    query = """
    INSERT INTO appointments (appointmentID,appointmentDate, appointmentTime, patientID, doctorID)
    VALUES (%s,%s, %s, %s, %s)
    """
    data = ( appointment_id,appointment_date, appointment_time, patient_id, doctor_id)
    
    conn = create_connection()
    execute_query(conn, query, data)
    conn.close()

    return redirect(url_for('index'))

@app.route('/add_diagnosis', methods=['POST'])
def add_diagnosis():
    diagnosis_id= request.form['diagnosisID']
    diagnosis_description = request.form['diagnosisDescription']
    appointment_id = request.form['appointmentID']

    query = """
    INSERT INTO diagnosis (diagnosisID,diagnosisDescription, appointmentID)
    VALUES (%s,%s, %s)
    """
    data = (diagnosis_id,diagnosis_description, appointment_id)
    
    conn = create_connection()
    execute_query(conn, query, data)
    conn.close()

    return redirect(url_for('index'))

@app.route('/add_treatment', methods=['POST'])
def add_treatment():
    treatment_id= request.form['treatmentID']
    treatment_description = request.form['treatmentDescription']
    appointment_id = request.form['appointmentID']

    query = """
    INSERT INTO treatment (treatmentid,treatmentDescription, appointmentID)
    VALUES (%s,%s, %s)
    """
    data = (treatment_id,treatment_description, appointment_id)
    
    conn = create_connection()
    execute_query(conn, query, data)
    conn.close()

    return redirect(url_for('index'))

@app.route('/add_prescription', methods=['POST'])
def add_prescription():
    prescription_id= request.form['prescriptionID']
    prescription_medication = request.form['prescriptionMedication']
    prescription_dosage = request.form['prescriptionDosage']
    appointment_id = request.form['appointmentID']

    query = """
    INSERT INTO prescription (prescriptionID,prescriptionMedication, prescriptionDosage, appointmentID)
    VALUES (%s,%s, %s, %s)   
    """
    data = (prescription_id,prescription_medication, prescription_dosage, appointment_id)
    
    conn = create_connection()
    execute_query(conn, query, data)
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
