const express = require('express');
const axios = require('axios');
const app = express();
const port = 3001;

app.use(express.json());
app.use(express.static('public'));

// Configuración del API principal
const API_BASE_URL = 'http://localhost:5000/api';

// Endpoint para listar alumnos
app.get('/alumnos', async (req, res) => {
    try {
        const response = await axios.get(`${API_BASE_URL}/alumnos`);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Endpoint para agregar alumno
app.post('/alumnos', async (req, res) => {
    try {
        const response = await axios.post(`${API_BASE_URL}/alumnos`, req.body);
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Endpoint para prueba de estrés
app.post('/alumnos/generar-masivos', async (req, res) => {
    try {
        const cantidad = req.body.cantidad || 1000;
        const response = await axios.post(`${API_BASE_URL}/alumnos/generar-masivos`, { cantidad });
        
        // Agregar métricas adicionales
        const metrics = {
            ...response.data,
            fecha: new Date().toISOString(),
            cantidad_solicitada: cantidad
        };
        
        res.json(metrics);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.listen(port, () => {
    console.log(`Microservicio corriendo en http://localhost:${port}`);
});