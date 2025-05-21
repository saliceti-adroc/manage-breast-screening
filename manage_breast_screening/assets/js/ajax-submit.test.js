import { getByRole } from '@testing-library/dom'
import { userEvent } from '@testing-library/user-event'

import { init } from './ajax-submit.js'

describe('AJAX submit', () => {
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
      <div class="app-ajax-submit" data-module="app-ajax-submit">
        <div data-hide-on-submit>Not submitted</div>
        <div data-show-on-submit hidden>Submitted</div>
        <form method="post" action="/example" data-success="container" novalidate>
          <button>Submit</button>
        </form>
      </div>
    `

    const $container = document.querySelector('[data-module="app-ajax-submit"]')

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

  it('refreshes the page if the request fails', async () => {
    const response = { ok: false, status: 500 }

    mockFetch(response)
    init()

    await user.click(button)

    expect(location.reload).toHaveBeenCalled()
    expect(message).toHaveAttribute('hidden')
    expect(oldMessage).not.toHaveAttribute('hidden')

    expect(console.error).toHaveBeenCalledWith(
      new Error(`Response status: ${response.status}`)
    )
  })

  it('refreshes the page if there is an error, such as a timeout', async () => {
    const error = new Error('Something went wrong')

    mockFetchRejected(error)
    init()

    await user.click(button)

    expect(location.reload).toHaveBeenCalled()
    expect(message).toHaveAttribute('hidden')
    expect(oldMessage).not.toHaveAttribute('hidden')

    expect(console.error).toHaveBeenCalledWith(error)
  })
})
