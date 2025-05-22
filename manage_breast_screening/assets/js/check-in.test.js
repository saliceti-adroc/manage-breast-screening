import { getByRole } from '@testing-library/dom'
import { userEvent } from '@testing-library/user-event'

import { init } from './check-in.js'

describe('Check in', () => {
  const user = userEvent.setup()

  /** @type {HTMLFormElement} */
  let form

  /** @type {HTMLButtonElement} */
  let button

  /** @type {HTMLDivElement} */
  let oldMessage

  /** @type {HTMLDivElement} */
  let message

  beforeEach(() => {
    document.body.innerHTML = `
      <div data-module="app-check-in">
        <div data-hide-on-submit>Not submitted</div>
        <div data-show-on-submit hidden>Submitted</div>
        <form method="post" action="/example" novalidate>
          <button>Submit</button>
        </form>
      </div>
    `

    const $container = document.querySelector('[data-module="app-check-in"]')

    form = $container.querySelector('form')
    button = getByRole(form, 'button', { name: 'Submit' })
    oldMessage = $container.querySelector('[data-hide-on-submit]')
    message = $container.querySelector('[data-show-on-submit]')

    jest.spyOn(console, 'error').mockImplementation(() => {})
  })

  it('swaps the form for a success message', async () => {
    mockFetch({ ok: true, status: 200 })
    init()

    await user.click(button)

    expect(form).toHaveAttribute('hidden')
    expect(oldMessage).toHaveAttribute('hidden')
    expect(message).not.toHaveAttribute('hidden')
    expect(console.error).not.toHaveBeenCalled()
  })

  it('does not change the DOM if the request fails', async () => {
    const response = { ok: false, status: 500 }

    mockFetch(response)
    init()

    await user.click(button)

    expect(message).toHaveAttribute('hidden')
    expect(oldMessage).not.toHaveAttribute('hidden')

    expect(console.error).toHaveBeenCalledWith(
      new Error(`Response status: ${response.status}`)
    )
  })
})
