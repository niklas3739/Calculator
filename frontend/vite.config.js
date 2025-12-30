import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  preview: {
    host: true,              // listen on 0.0.0.0
    port: 4173,              // default, Railway will override via --port $PORT anyway
    allowedHosts: [
      "calculator-frontend-production.up.railway.app",
      ".up.railway.app",     // allow any Railway subdomain (handy if it changes)
      "localhost",
    ],
  },
});