import '@testing-library/jest-dom'

/**
 * Mock fetch() function for jsdom
 */
Object.defineProperty(window, 'fetch', {
  configurable: true,
  writable: true,
  value: jest.fn().mockResolvedValue(undefined)
})
