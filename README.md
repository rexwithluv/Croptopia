# Croptopia searcher

Esta pequeña aplicación basada en el mod [Croptopia](https://github.com/ExcessiveAmountsOfZombies/Croptopia) de Minecraft permite introducir uno o más ingredientes y devuelve las recetas que los contienen aunque no sea en su totalidad.

## Desplegar
```
docker compose -d --build
```

## Tecnologías usadas:
- Para el Backend:
    - Flask (Python)
    - JSON como BD
- Para el Frontend:
    - HTML
    - Bulma (CSS)

## Estructura de archivos
```
│
├── templates/
│    └── index.html
├── app.py
├── docker-compose.yml
├── Dockerfile
├── README.md
├── recipes.json
├── requirements.txt

```