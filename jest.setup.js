import '@testing-library/jest-dom'

/**
 * Mock fetch() function for jsdom
 */
global.mockFetch = (response) => {
  Object.defineProperty(window, 'fetch', {
    configurable: true,
    writable: true,
    value: jest.fn().mockResolvedValueOnce(response)
  })
}

global.mockFetchRejected = (response) => {
  Object.defineProperty(window, 'fetch', {
    configurable: true,
    writable: true,
    value: jest.fn().mockRejectedValueOnce(response)
  })
}

afterEach(() => {
  if (window.fetch !== undefined) delete window.fetch
})
