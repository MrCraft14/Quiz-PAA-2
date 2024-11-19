def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Membagi array menjadi dua bagian
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Rekursif memanggil merge_sort untuk kedua bagian
        merge_sort(left_half)
        merge_sort(right_half)

        # Menggabungkan kembali bagian-bagian yang sudah diurutkan
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Menyalin elemen yang tersisa di left_half (jika ada)
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Menyalin elemen yang tersisa di right_half (jika ada)
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Basis rekursi, array dengan 0 atau 1 elemen sudah terurut
    else:
        pivot = arr[len(arr) // 2]  # Memilih pivot di tengah
        left = [x for x in arr if x < pivot]  # Elemen lebih kecil dari pivot
        middle = [x for x in arr if x == pivot]  # Elemen sama dengan pivot
        right = [x for x in arr if x > pivot]  # Elemen lebih besar dari pivot
        return quick_sort(left) + middle + quick_sort(right)
# Data
X = [1, 5, 6, 4, 3, 3, 7, 7, 9, 0, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Menggunakan Merge Sort
sorted_merge = merge_sort(X.copy())
print("Hasil Merge Sort:", sorted_merge)

# Menggunakan Quick Sort
sorted_quick = quick_sort(X.copy())
print("Hasil Quick Sort:", sorted_quick)


# Analisa Worst Case, Best Case, dan Average Case dari Merge Sort    
# Worst Case: O (nlogn) terjadi pada semua jenis input karena sifat rekursifnya.
# Best Case: O (nlogn) karena tetap melakukan pembagian dan penggabungan terlepas dari kondisi input.
# Average Case: O (nlog⁡n) terjadi pada input acak.

# Analisa Worst Case, Best Case, dan Average Case dari Quick Sort
# Worst Case: O(n^2) terjadi jika pivot yang dipilih adalah elemen terkecil atau terbesar, misalnya pada array yang sudah terurut.
# Best Case: O(nlog⁡n) jika pivot selalu berada di tengah, membagi array secara seimbang.
# Average Case: O(nlog⁡n) pada input acak.

