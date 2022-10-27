void main(){
 var vehiculo = Vehiculo;
  vehiculo.marca = "Toyota";
  vehiculo.modelo = "Corolla";
  vehiculo.color = 'Blanco';
  vehiculo.llantas = 4;

}

void showVehiculo(){
   
  print("Marca: ${Vehiculo.marca}");
  print("Modelo: ${Vehiculo.modelo}");
  print("Color: ${Vehiculo.color}");
  print("Llantas: ${Vehiculo.llantas}");
}

class Vehiculo{
  int _llantas;
  String _color;
  String _modelo;
  String _marca;

  void set llantas(int llantas) => _llantas = llantas;
  void set color(String color) => _color = color;
  void set modelo(String modelo) => _modelo = modelo;
  void set marca(String marca) => _marca = marca;

  String get color => _color;
  String get marca => _marca;
  String get modelo => _modelo;
  int get llantas => _llantas;

  // Vehiculo (int llantas, String color, String modelo, String marca){
  //  this._llantas = llantas;
  //  this._color = color;
  //  this._modelo = modelo;
  //  this._marca = marca;
  // }

  Vehiculo(this._llantas, this._color, this._modelo, this._marca);
  Vehiculo.marca(this._marca);

  void arrancar(){
    print("El vehiculo esta arrancando");
  }
  void correr(){
    print("El vehiculo esta corriendo");
  }
  void frenar(){
    print("El vehiculo esta frenando");
  }
}