const express = require('express');
const morgan = require("morgan");
const { createProxyMiddleware } = require('http-proxy-middleware');
const cors = require('cors')


// Create Express Server
const app = express();
const SocketServer = require('ws').Server;

// Configuration
const PORT = 6969;
const HOST = "0.0.0.0";

const API_SERVICE_URL = `http://${process.env.TARGET_HOST}:${process.env.TARGET_PORT}`;

app.use(cors())
app.options('*', cors()) // include before other routes


// Logging
app.use(morgan('dev'));

 // Proxy endpoints
app.use('/api', createProxyMiddleware({
    target: API_SERVICE_URL,
    changeOrigin: true,
    pathRewrite: {
        [`^/api`]: '',
    },
 }));

 // Start the Proxy
let server = app.listen(PORT, HOST, () => {
    console.log(`Starting Proxy at ${HOST}:${PORT}`);
 });

 const wss = new SocketServer({ server });