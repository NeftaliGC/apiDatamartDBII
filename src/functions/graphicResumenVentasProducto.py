import matplotlib.pyplot as plt
import io

class GraphicResumenVentasProducto:
    def __init__(self, data):
        self.data = data

    def generate(self):
        self.productos = [item[0] for item in data if item[0] is not None]
        self.ventas = [item[1] for item in data if item[1] is not None]

        plt.figure(figsize=(10, 5))
        plt.bar(self.productos, self.ventas, color='blue')
        plt.xlabel('Productos')
        plt.ylabel('Ventas')
        plt.title('Desglose Completo de Ventas por Producto')
        plt.xticks(rotation=45, ha='right')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        return StreamingResponse(buf, media_type='image/png')
