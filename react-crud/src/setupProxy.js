const { createProxyMiddleware } = require("http-proxy-middleware");

module.exports = function(app) {
  app.use(
    "/api",
    createProxyMiddleware({
    //   target: "http://backend:8000",
      target: "http://172.17.0.3:8000",
      pathRewrite: { "^/api": "" }
    })
  );
};


/** https://stackoverflow.com/questions/58431098/create-react-app-http-proxy-middleware-not-working */