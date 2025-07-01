// Simple Frontend Configuration
class Config {
    constructor() {
        this.config = {
            BACKEND_URL: 'http://127.0.0.1:8000',
            ENABLE_AI_FEATURES: true,
            ENABLE_SECURITY_ALERTS: true
        };
    }

    get(key) {
        return this.config[key];
    }

    // Backend URL for API calls
    getBackendUrl() {
        return this.get('BACKEND_URL');
    }

    // Check if AI features are enabled (API key handled by backend)
    isAIEnabled() {
        return this.get('ENABLE_AI_FEATURES');
    }

    // Check if security alerts are enabled
    isSecurityAlertsEnabled() {
        return this.get('ENABLE_SECURITY_ALERTS');
    }
}

// Create global configuration instance
const config = new Config();
window.config = config;
