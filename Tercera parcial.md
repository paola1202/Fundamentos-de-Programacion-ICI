# Fundamentos de programación 
## Actividades tercera parcial
###  Actividad 1
```elixir
# ACT 1 Hacer un programa recursivo que imprima n veces un mensaje 
defmodule Repetir do
    def imprimir(msg,n) when n<=1 do
        IO.puts("#{n}: #{msg}")
    end

    def(msg,n) do
        IO.puts("#{n}: #{msg}")
        imprimir(msg,n-1)
    end
end

Repetir.imprimir("Hola",10)
```

### Actividad 2
```elixir
# ACT 2  Invertir el orden de los numeros 
defmodule Repetir do
    def imprimir(msg,n,ls) when n>=ls do
        IO.puts("#{n}: #{msg}")
        imprimir(msg, n+1, ls)
    end
end

Repetir.imprimir("Hola,1,10")
```

### Actividad 3
```elixir
# ACT 3  Escribir un programa recursivo que sume todos los elementos de una serie de numeros en una lista
defmodule Matematicas do
    def sum_list([], suma), do: suma
    def sum_list([head|tail], suma) do
        sum_list(tail, suma+head)
    end
end
IO.puts(Matematicas.sum_list([1,2,3,4,5,6,7,8,9,10],0))
IO.puts(Matematicas.sum_list([1,3,5,7,9,10,15],0))
```

### Actividad 4
```elixir
# ACT 4  Obtener el promedio de 10 calificaciones entre 0 y 10 almacenadas en una lista 
defmodule Matematicas do
    def sum_list([], suma), do: suma
    def sum_list([head|tail], suma) do
        sum_list(tail, suma+head)
    end
end
IO.puts(Matematicas.sum_list([10,5,9,9,8,5,7,9,6,5],0)/10)
```

### Actividad 5
```elixir
# ACT 5 Crear una funcion que calcule el promedio de 10 calificaciones almacenadas en una lista entre 0 y 10
defmodule Matematicas do
    def sum_list([],suma), do: suma
    def sum_list([head  tail], suma) do
        sum_list(tail, suma+head)
    end
    def promedio(calificaciones, n) do
        sum_list(calificaciones,0)/n
    end
end
IO.puts(Matematicas.promedio([10,5,9,9,8,5,7,9,6,5],10))
```

### Actividad 6
```elixir
# ACT 6 Calcular el promedio de n calificaciones entre 0 y 10 en una lista 

defmodule Matematicas do
    def sum_list([], suma), do: suma
    def sum_list([head|tail], suma) do  
        sum_list(tail, suma+head)
    end 
    def promedio(calificaciones) do
        sum_list(calificaciones,0)/Enum.count(calificaciones)
    end
end 
IO.puts(Matematicas.promedio([10,5,9,9,8,5,7,9,6,5]))
```

### Actividad 7
```elixir
# ACT 7 La forma mas sencilla es mediente el modulo "Enum"

calificaciones = [10,5,9,9,8,5,7,9,6,5]
IO.puts Enum.sum(calificaciones)/Enum.count(calificaciones)
```

### Actividad 8
```elixir
# ACT 8 Generar n calificaciones aleatorias entre 0 y 10 y obtener su promedio

max = 50
calificaciones = for _x <- 1..max do
    Enum.random(0..10)
end
IO.inspect(calificaciones)
IO.puts Enum.count(calificaciones)
IO.puts Enum.sum(calificaciones)/Enum.count(calificaciones)
```

### Actividad 9
```elixir
# ACT 9 Escriba el problema anterior con un modulo y una funcion, recibiendo como argumentos la cantidad de calificaciones a generar, así como el rango de calificaciones

defmodule Estadistica do
    def promedio(max_cal, _li, _ls) when max_cal <= 1 do
        :error
    end
    def promedio(max_cal, _li, _ls) when max_cal > 1 do
        calificaciones = for _x <- 1..max_cal do
            Enum.random(li..ls)
        end
        Enum.sum(calificaciones)/Enum.count(calificaciones)
    end
end
```

### Actividad 10
```elixir
# ACT 10 Hacer un programa recursivo que cuente de manera creciente de li (limite inferior) a ls (limite superior) para li>=ls inclusive

defmodule For_range do
    def for_to(n, ls) when n > ls do
        IO.puts "error"
    end
    def for_to(n,ls) when n >= ls do
        IO.puts n
    end 
    def for_to(n, ls) do
        IO.puts n
        for_to(n + 1, ls)
    end 
end 
IO.puts("contar de 1 a 10")
For_range.for_to(1,10)

IO.puts("contar de 12 a 5")
For_range.for_to(12,5)
```

### Actividad 11
```elixir
# ACT 11 Programa que sume los valores de los numeros consecutivos entre li y ls inclusive

defmodule For_range do  
    def for_to(n,ls) when n>= ls do
        n
    end 

    def for_to(n,ls) do
        n + for_to(n + 1,ls)
    end
end 
IO.puts("suma de los numeros de 1 a 10")
IO.puts For_range.for_to(5,12)

IO.puts("suma de los numeros 5 a 12")
IO.puts For_range.for_to(5,12)
```
