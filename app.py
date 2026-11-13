from flask import Flask, render_template_string

app = Flask(__name__)

# Website ဒီဇိုင်းနဲ့ ချော့မယ့်စာသားများ (HTML + CSS + JS)
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="my">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ကိုယ့်ကို စိတ်မဆိုးပါနဲ့တော့နော် 🥺❤️</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Padauk:wght@400;700&display=swap');

        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
            font-family: 'Padauk', sans-serif;
            overflow: hidden;
            text-align: center;
        }

        .card {
            background: rgba(255, 255, 255, 0.9);
            padding: 40px 30px;
            border-radius: 25px;
            box-shadow: 0 15px 35px rgba(255, 105, 135, 0.25);
            max-width: 400px;
            width: 85%;
            position: relative;
            z-index: 10;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }

        .emoji {
            font-size: 65px;
            margin-bottom: 10px;
            display: block;
        }

        h1 {
            color: #e11d48;
            font-size: 24px;
            margin-bottom: 15px;
        }

        p {
            color: #4b5563;
            font-size: 16px;
            line-height: 1.7;
            margin-bottom: 25px;
        }

        .btn-group {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }

        button {
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-family: 'Padauk', sans-serif;
            transition: all 0.3s ease;
        }

        #yesBtn {
            background-color: #ff4d6d;
            color: white;
            box-shadow: 0 5px 15px rgba(255, 77, 109, 0.4);
        }

        #yesBtn:hover {
            background-color: #e01e37;
            transform: scale(1.08);
        }

        #noBtn {
            background-color: #e5e7eb;
            color: #374151;
            position: relative;
        }

        /* ခွင့်လွှတ်လိုက်ရင် ပေါ်လာမယ့် စာသား */
        #successMessage {
            display: none;
        }
    </style>
</head>
<body>

    <div class="card" id="mainCard">
        <span class="emoji">🥺👉👈</span>
        <h1>ကိုယ့်ကို စိတ်ဆိုးပြေပါတော့နော်...</h1>
        <p>
            ကိုယ်မှားသွားပါတယ်ကွာ... မင်းစိတ်ဆိုးနေရင် ကိုယ့်မှာ ဘာမှလုပ်လို့မရဘဲ စိတ်တွေပူနေရလို့ပါ။ <br>
            <b>အရမ်းချစ်တယ်နော် ❤️</b> စိတ်ဆိုးပြေပေးပါတော့...
        </p>
        <div class="btn-group">
            <button id="yesBtn" onclick="forgiveMe()">ခွင့်လွှတ်တယ် ❤️</button>
            <button id="noBtn" onmouseover="moveButton()" onclick="moveButton()">မခွင့်လွှတ်ဘူး 😤</button>
        </div>
    </div>

    <div class="card" id="successMessage">
        <span class="emoji">🥰🎉💖</span>
        <h1>ရေးးး! ကျေးဇူးအများကြီးတင်ပါတယ်!</h1>
        <p>
            ကိုယ့်ရဲ့ အချစ်ဆုံးလေးက သဘောအကောင်းဆုံးပဲ။ <br>
            နောက်ဆို မင်းစိတ်ဆိုးအောင် မလုပ်တော့ပါဘူးလို့ ကတိပေးပါတယ်ဗျာ။ အာဘွားး 😘❤️
        </p>
    </div>

    <script>
        // "မခွင့်လွှတ်ဘူး" ခလုတ်ကို ထွက်ပြေးအောင်လုပ်ခြင်း
        function moveButton() {
            const noBtn = document.getElementById('noBtn');
            const x = Math.random() * (window.innerWidth - noBtn.offsetWidth - 40);
            const y = Math.random() * (window.innerHeight - noBtn.offsetHeight - 40);

            noBtn.style.position = 'fixed';
            noBtn.style.left = x + 'px';
            noBtn.style.top = y + 'px';
        }

        // "ခွင့်လွှတ်တယ်" နှိပ်လိုက်ရင် စာသားပြောင်းပေးခြင်း
        function forgiveMe() {
            document.getElementById('mainCard').style.display = 'none';
            document.getElementById('successMessage').style.display = 'block';
        }
    </script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)


if __name__ == "__main__":
    app.run(debug=True)