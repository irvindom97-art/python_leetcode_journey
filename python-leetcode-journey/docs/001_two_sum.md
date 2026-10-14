# LeetCode #1 — Two Sum | Suma de dos

**Topics / Temas:** Array (lista), Hash Map (diccionario)  
**Difficulty / Dificultad:** Easy / Fácil

## 1. Problem | Problema

**English:** Given an integer array `nums` and an integer `target`, return the indices of two different elements whose values add up to `target`. Assume there is exactly one valid solution, and do not use the same element twice.

**Español:** Dada una lista de enteros `nums` y un entero `target`, devuelve los índices de dos elementos diferentes cuya suma sea igual a `target`. Se asume que existe exactamente una solución válida y que no se puede utilizar el mismo elemento dos veces.

### Example | Ejemplo

```text
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

## 2. Understand the task | Entender el problema

We need the **indices**, not the values themselves. For every value `x`, the value we need to complete the sum is its complement:

`complement = target - x`

Necesitamos devolver los **índices**, no los valores. Para cada valor `x`, el número que falta para completar la suma es su complemento:

`complement = target - x`

## 3. Approach | Estrategia

### Step-by-step | Paso a paso

1. Create an empty dictionary called `seen`. It will map a number to the index where we first saw it.  
   Creamos un diccionario vacío llamado `seen`, que relaciona cada número con el índice donde apareció.

2. Iterate through `nums` using `enumerate`, which gives us both `index` and `value`.  
   Recorremos `nums` con `enumerate`, que nos da tanto `index` como `value`.

3. Calculate `complement = target - value`.  
   Calculamos el complemento que necesitamos.

4. Check whether `complement` is already in `seen`. If so, the earlier index and the current index form the answer.  
   Comprobamos si el complemento ya está en `seen`. Si existe, el índice guardado y el índice actual forman la respuesta.

5. If the complement is not present, save the current value and its index in `seen`.  
   Si todavía no existe, guardamos el valor actual y su índice en el diccionario.

6. If the loop finishes without a solution, raise an error. The standard LeetCode problem guarantees a valid answer, but the explicit error makes this reusable function clearer outside that context.  
   Si el recorrido termina sin solución, lanzamos un error. LeetCode garantiza una respuesta válida en el problema original, pero el error explícito hace que la función sea más clara al reutilizarla.

## 4. Walkthrough | Recorrido manual

Input / Entrada: `nums = [2, 7, 11, 15]`, `target = 9`

| Step / Paso | Index / Índice | Value / Valor | Complement | `seen` before check | Action / Acción |
|---|---:|---:|---:|---|---|
| 1 | 0 | 2 | 7 | `{}` | 7 is absent; save `2: 0` |
| 2 | 1 | 7 | 2 | `{2: 0}` | 2 exists; return `[0, 1]` |

In step 2, `9 - 7 = 2`. The dictionary already contains `2` at index `0`, so the answer is `[0, 1]`.

En el paso 2, `9 - 7 = 2`. El diccionario ya contiene el número `2` en el índice `0`, por lo que devolvemos `[0, 1]`.

## 5. Python solution | Solución en Python

```python
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}

    for index, value in enumerate(nums):
        complement = target - value

        if complement in seen:
            return [seen[complement], index]

        seen[value] = index

    raise ValueError("No two-sum solution exists for the given input.")
```

### Key concepts | Conceptos clave

- `enumerate(nums)`: iterates over values and indices. / Recorre valores e índices.
- `dict`: provides average-case constant-time lookups. / Permite búsquedas en tiempo promedio constante.
- `return`: stops the function as soon as the pair is found. / Finaliza la función al encontrar el par.
- The check happens **before** saving the current value, so the same element is not used twice. / La comprobación se hace **antes** de guardar el valor actual, evitando reutilizar el mismo elemento.

## 6. Complexity analysis | Análisis de complejidad

- **Time / Tiempo: `O(n)` average.** We traverse the list at most once, and dictionary lookups and insertions take `O(1)` on average.
- **Space / Espacio: `O(n)`.** In the worst case, the dictionary stores up to `n` values.

- **Tiempo: `O(n)` promedio.** Recorremos la lista como máximo una vez y las búsquedas e inserciones en el diccionario son `O(1)` en promedio.
- **Espacio: `O(n)`.** En el peor caso, el diccionario almacena hasta `n` valores.

## 7. Test cases | Casos de prueba

| Input / Entrada | Target | Expected output / Salida esperada | Purpose / Propósito |
|---|---:|---|---|
| `[2, 7, 11, 15]` | 9 | `[0, 1]` | Basic case / Caso básico |
| `[3, 2, 4]` | 6 | `[1, 2]` | Pair not adjacent / Par no adyacente |
| `[3, 3]` | 6 | `[0, 1]` | Duplicate values / Valores repetidos |
| `[-1, -2, -3, -4, -5]` | -8 | `[2, 4]` | Negative numbers / Números negativos |

## 8. Common mistakes | Errores comunes

1. Returning the values instead of their indices. / Devolver los valores en vez de sus índices.
2. Checking only the current value without calculating the complement. / No calcular el complemento.
3. Saving the current value before checking the complement, which can incorrectly allow reusing the same element in variants of the problem. / Guardar el valor antes de comprobar el complemento puede permitir reutilizar el mismo elemento en variantes del problema.
4. Claiming `O(n²)` for this dictionary-based approach. The nested-loop brute-force approach is `O(n²)`; this approach is `O(n)` average time. / Confundir esta estrategia con fuerza bruta, que sí tiene complejidad `O(n²)`.

## 9. What I learned | Qué aprendí

**English**
- A hash map can reduce a pair-search problem from quadratic time to linear average time.
- The complement transforms the question “Which pair adds up to the target?” into “Have I already seen the number I need?”
- `enumerate` is useful when both the value and its index are needed.

**Español**
- Un diccionario puede reducir la búsqueda de un par de tiempo cuadrático a tiempo lineal promedio.
- El complemento convierte la pregunta «¿qué par suma el objetivo?» en «¿ya encontré el número que necesito?».
- `enumerate` es útil cuando necesitamos tanto el valor como su índice.

## 10. Interview explanation | Explicación para entrevista

**English:** “I use a hash map to store each number and its index as I traverse the array. For each number, I calculate the complement needed to reach the target. If that complement is already in the map, I return the stored index and the current index. This gives `O(n)` average time complexity and `O(n)` space complexity.”

**Español:** «Utilizo un diccionario para guardar cada número y su índice mientras recorro la lista. Para cada número calculo el complemento necesario para alcanzar el objetivo. Si ese complemento ya está en el diccionario, devuelvo el índice almacenado y el índice actual. Esto ofrece complejidad temporal promedio `O(n)` y espacial `O(n)`.»

## Source | Fuente

Problem reference: [LeetCode #1 — Two Sum](https://leetcode.com/problems/two-sum/). The explanation above is paraphrased for learning.
