import { waitFor } from '@testing-library/dom'

import { initCheckIn } from './check-in.js'

jest.mock('./check-in.js')

describe('Automatic initialisation', () => {
  it('should init components on DOMContentLoaded', async () => {
    await import('./index.js')

    // Should not initialise on import
    expect(initCheckIn).not.toHaveBeenCalled()

    // Should initialise on DOMContentLoaded
    window.document.dispatchEvent(new Event('DOMContentLoaded'))
    await waitFor(() => expect(initCheckIn).toHaveBeenCalled())
  })
})
