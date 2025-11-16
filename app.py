from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        names = request.form["names"].splitlines()
        group_size = int(request.form["group_size"])
        
        # Acak urutan nama
        random.shuffle(names)
        
        steps = []  # Menyimpan proses pengelompokan setiap langkah
        groups = []
        
        # Memulai proses pengelompokan
        current_group = []  # Grup sementara
        for i, name in enumerate(names, start=1):
            current_group.append(name)  # Tambahkan nama ke grup saat ini
            steps.append(f"Langkah {i}: Menambahkan '{name}' ke grup saat ini: {current_group}")
            
            # Jika grup sementara mencapai ukuran yang diinginkan atau jika itu nama terakhir
            if len(current_group) == group_size or i == len(names):
                groups.append(current_group[:])  # Tambahkan salinan grup sementara ke hasil akhir
                steps.append(f"Grup terbentuk: {current_group}")
                current_group = []  # Reset grup sementara untuk grup berikutnya

        return render_template("index.html", groups=groups, steps=steps)

    return render_template("index.html", groups=None, steps=None)

if __name__ == "__main__":
    app.run(debug=True)
  
