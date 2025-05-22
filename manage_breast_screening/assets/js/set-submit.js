const TIMEOUT = 2000

/**
 * Enable a form to be submitted in the background via `fetch()`.
 * If this fails for any reason, it will fall back to normal form submission
 * (this assumes the form action is idempotent)
 *
 * @param {HTMLFormElement} $form - HTML form element
 * @param {object} [options] - Handler options
 * @param {(this: HTMLFormElement) => void} [options.onBeforeSubmit] - Callback before submission
 * @param {(this: HTMLFormElement, response: Response) => void} [options.onSuccess] - Callback on successful response
 * @param {(this: HTMLFormElement, error: any) => void} [options.onError] - Callback on error
 */
export default ($form, options = {}) => {
  if (!$form || !($form instanceof HTMLFormElement)) {
    throw Error('setSubmit must be called with an HTMLFormElement')
  }

  const method = $form.method
  const action = $form.action

  if (!method || !action) {
    throw Error('Form method and action must be defined')
  }

  const doSubmit = async () => {
    if (options.onBeforeSubmit) {
      options.onBeforeSubmit.call($form)
    }

    const fetchOptions = { method: method, body: new FormData($form) }
    if (AbortSignal.timeout !== undefined) {
      fetchOptions.signal = AbortSignal.timeout(TIMEOUT)
    }

    let response
    try {
      response = await fetch(action, fetchOptions)

      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`)
      }
    } catch (e) {
      if (options.onError) {
        options.onError.apply($form, [e])
      }
      return
    }

    if (options.onSuccess) {
      try {
        options.onSuccess.apply($form, [response])
      } catch (e) {
        console.warn(
          'setSubmit: the form was submitted successfully, but the onSuccess handler threw an exception.'
        )
      }
    }
  }

  $form.addEventListener('submit', (event) => {
    doSubmit()
    event.preventDefault()
  })
}
