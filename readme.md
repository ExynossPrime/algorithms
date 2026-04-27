```mermaid
graph TD
    A[Начало] --> B[Ввод 4 элементов<br/>array = [input() ×4]]
    B --> C[dict = {}]
    C --> D{for i in array}
    D -->|да| E[a = 0]
    E --> F{for j in range(len(array))}
    F -->|да| G{i == array[j]?}
    G -->|да| H[a += 1]
    H --> F
    G -->|нет| F
    F -->|нет| I{a > 1?}
    I -->|да| J[dict[i] = a]
    J --> D
    I -->|нет| D
    D -->|нет| K{not dict?}
    K -->|да| L[print<br/>"Нет повторяющихся значений"]
    K -->|нет| M[for i in dict:<br/>print f"Число {i}<br/>встречается {dict[i]} раза"]
    L --> P[Конец]
    M --> P[Конец]
```
