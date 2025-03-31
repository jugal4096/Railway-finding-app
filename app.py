from flask import Flask, request, jsonify
import oracledb
from datetime import datetime

app = Flask(__name__)

# Oracle DB Connection
def get_db_connection():
    return oracledb.connect(user="system", password="jugal", dsn="localhost:1521/xe")

@app.route('/get_trains', methods=['GET'])
def get_trains():
    try:
        user_time = request.args.get('time')
        selected_day = request.args.get('day')

        if not user_time or not selected_day:
            return jsonify({'error': 'Missing time or day parameter'}), 400

        input_time = datetime.strptime(user_time, "%H:%M").time()

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            SELECT TRAIN_NAME, TRAIN_NUMBER, TO_CHAR(DEPARTURE_TIME, 'HH24:MI'), 
                   TO_CHAR(ARRIVAL_TIME, 'HH24:MI'), SOURCE, DESTINATION, DAYS
            FROM train
            WHERE SOURCE = 'Jalna' 
              AND DESTINATION = 'Aurangabad'
              AND TO_CHAR(DEPARTURE_TIME, 'HH24:MI') >= :time
              AND INSTR(DAYS, :day) > 0
            ORDER BY DEPARTURE_TIME
        """
        cursor.execute(query, {'time': user_time, 'day': selected_day})

        trains = []
        for row in cursor.fetchall():
            train = {
                'train_name': row[0],
                'train_number': row[1],
                'departure_time': row[2],
                'arrival_time': row[3],
                'source': row[4],
                'destination': row[5],
                'days': row[6]
            }
            trains.append(train)

        conn.close()
        
        return jsonify(trains if trains else {'message': 'No trains available'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


