from flask import Flask, request, render_template, jsonify
import servo  # servo.py 모듈 불러오기

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/angle', methods=['POST'])
def control_servo():
    data = request.get_json()

    if not data or 'angle' not in data:
        return jsonify({'status': 'fail', 'message': 'angle 파라미터가 없습니다.'}), 400

    try:
        angle = int(data.get('angle'))

        if 0 <= angle <= 180:
            servo.setAngle(angle)  # servo.py의 set_angle 함수 실행
            return jsonify({'status': 'success', 'message': f'각도가 {angle}도로 설정되었습니다.'}), 200
        else:
            return jsonify({'status': 'fail', 'message': '0에서 180 사이의 숫자만 가능합니다.'}), 400

    except (ValueError, TypeError):
        return jsonify({'status': 'fail', 'message': '올바른 숫자를 입력해 주세요.'}), 400

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5001, debug=True)
    finally:
        servo.cleanup()  # 서버 종료 시 GPIO cleanup
