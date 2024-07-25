// Router: Routes the endpoints to use the appropriate Controller method

const express = require('express');
const router = express.Router();
const Controller = require('../controller');

// DB 
router.get('/status', Controller.getStatus);
router.get('/stats', Controller.getStats);

module.exports = router;
