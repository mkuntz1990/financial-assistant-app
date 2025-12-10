# Test Data for Frontend Components

This file provides mock data for frontend components, supporting development and testing of UI features without requiring a live backend.

- `mockData.js`: Exports mock responses for version, update, health, and ping endpoints.

## Usage

Import the mock data in your frontend components or tests as needed:

```js
import { MOCK_VERSION, MOCK_UPDATE, MOCK_HEALTH, MOCK_PING } from './mockData';
```

This allows you to develop and test UI features in isolation, ensuring new features are covered by test data.
