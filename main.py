from flask import Flask, render_template, request
import random
app = Flask(__name__)
words = ["Sun", "Moon", "Star", "Nova", "Sky", "Wave", "Cloud", "Fire", "Wind", "Light", "Blue", "Red"]
symbols = ["!", "@", "#", "$", "%", "&"]

@app.route("/", methods=["GET", "POST"])
def password():
    generated_password = ""

    if request.method == "POST":
        # Read user options
        use_lower = request.form.get("lowercase")
        use_upper = request.form.get("uppercase")
        use_numbers = request.form.get("numbers")
        use_symbols = request.form.get("symbols")
        length = int(request.form.get("length", 12))

        # Pick 2 random words
        word1 = random.choice(words)
        word2 = random.choice(words)

        # Apply uppercase/lowercase
        if use_lower and not use_upper:
            word1, word2 = word1.lower(), word2.lower()
        elif use_upper and not use_lower:
            word1, word2 = word1.upper(), word2.upper()
        # if both or none, keep original casing

        generated_password = word1 + word2

        # Add number if selected
        if use_numbers:
            generated_password += str(random.randint(10, 99))

        # Add symbol if selected
        if use_symbols:
            generated_password += random.choice(symbols)

        # Trim if longer than desired length
        if len(generated_password) > length:
            generated_password = generated_password[:length]

    return render_template("page.html", password=generated_password)

if __name__ == "__main__":
    app.run(debug=True)
