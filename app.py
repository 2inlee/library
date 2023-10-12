from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

members = {}  # {name: {"phone": phone, "borrowed_books": []}}
books = {}  # {title: {"borrowed_by": None}}

@app.route('/')
def index():
    return render_template('library.html')

@app.route('/add_member', methods=['POST'])
def add_member():
    name = request.form.get('member_name')
    phone = request.form.get('member_phone')
    if name in members:
        return jsonify({"message": "멤버가 이미 존재합니다."}), 400
    members[name] = {"phone": phone, "borrowed_books": []}
    return jsonify({"message": "멤버가 추가되었습니다."}), 201

@app.route('/delete_member', methods=['POST'])
def delete_member():
    name = request.form.get('member_name')
    if name not in members:
        return jsonify({"message": "멤버가 존재하지 않습니다."}), 404
    del members[name]
    return jsonify({"message": "멤버가 삭제되었습니다."}), 200

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form.get('book_title')
    if title in books:
        return jsonify({"message": "책이 이미 존재합니다."}), 400
    books[title] = {"borrowed_by": None}
    return jsonify({"message": "책이 추가되었습니다."}), 201

@app.route('/delete_book', methods=['POST'])
def delete_book():
    title = request.form.get('book_title')
    if title not in books:
        return jsonify({"message": "책이 존재하지 않습니다."}), 404
    del books[title]
    return jsonify({"message": "책이 삭제되었습니다."}), 200

@app.route('/borrow_book', methods=['POST'])
def borrow_book():
    member_name = request.form.get('member_name')
    book_title = request.form.get('book_title')
    if member_name not in members or book_title not in books:
        return jsonify({"message": "멤버 또는 책이 존재하지 않습니다."}), 404
    if books[book_title]['borrowed_by']:
        return jsonify({"message": "책이 이미 대출되었습니다."}), 400
    books[book_title]['borrowed_by'] = member_name
    members[member_name]['borrowed_books'].append(book_title)
    return jsonify({"message": "책이 대출되었습니다."}), 200

@app.route('/return_book', methods=['POST'])
def return_book():
    member_name = request.form.get('member_name')
    book_title = request.form.get('book_title')
    if member_name not in members or book_title not in books:
        return jsonify({"message": "멤버 또는 책이 존재하지 않습니다."}), 404
    if books[book_title]['borrowed_by'] != member_name:
        return jsonify({"message": "이 멤버가 대출한 책이 아닙니다."}), 400
    books[book_title]['borrowed_by'] = None
    members[member_name]['borrowed_books'].remove(book_title)
    return jsonify({"message": "책이 반납되었습니다."}), 200

@app.route('/status')
def status():
    return jsonify({"members": members, "books": books})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
