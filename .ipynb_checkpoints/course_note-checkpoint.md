# Data Visualization with Plotly in Python #

## Apa itu plotly? ##
* plotly adalah library visualisasi dari JavaScript.
* Namun dalam kasus ini kita tidak perlu mempelajari JS, kita akan menggunakan Python wrapper

## Mengapa menggunakan Plotly ##
* Cepat
* minim coding
* Punya banyak customisasi
* interaktif

## Tiga komponen grafik di plotly ##
* Layout --> styling
* Data --> untuk mengotrol jenis grafik dan data yang digunakan
* Frame --> untuk menganimasikan grafik

## Membuat grafik dengan plotly ##
Menggunakan graph_object akan memberikan kita lebih banyak kemungkinan kustomisasi. Namun untuk jumlah data yang sangat banyak, maka hal ini sukar untuk dilakukan. Oleh karena itu kita akan menggunakan plotly.express --> px
kapan kita akan menggunakan library express atau Graph_object?
* Ketika kita membutuhkan lebih banyak kostumisasi, maka kita gunakan graph_object (go)
* Ketika kita membutuhkan grafik yang cepat dibuat, kita gunakan px
* Ketika kita akan membuat subplot akan lebih mudah jika menggunakan go.
* Subplot menggunakan 1 index bukan 0 index

