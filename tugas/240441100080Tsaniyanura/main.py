nama1 = "tisa"
nama2 = "lisa"

print(f"{nama1} hai kamu sudah mengerjakan tugas makalah?")
print(f"{nama2} belum selesai,kamu sudah?")
print(f"{nama1} aku sudah")
print(f"{nama2} aku ada pertanyaannih")
print(f"{nama1} pertanyaan apa?")

print(f"{nama1} : 3 + 8 berapa?")
jawaban = int(input(f"{nama2} : "))
hasil = 3 + 8

if jawaban == hasil:
    print(f"{nama1} jawabanmu benar ")
else:
    print(f"{nama1} jawabanmu salah yang benar adalah {hasil}")
