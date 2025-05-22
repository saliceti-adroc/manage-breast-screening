import setSubmit from './set-submit.js'

/*
Enhance an HTML form to intercept submit events and instead fetch the form action URL.
If successful, show child elements with data-show-on-submit, and hide those with data-hide-on-submit.
If unsuccessful, or the fetch times out, force a page refresh.
*/
class CheckIn {
  constructor($root) {
    if (!$root) {
      throw Error('CheckIn initialised without a root element')
    }

    this.$root = $root
    this.$form = $root.querySelector('form')
    this.$showOnSubmit = $root.querySelectorAll('[data-show-on-submit]')
    this.$hideOnSubmit = $root.querySelectorAll('[data-hide-on-submit]')

    const showResult = this.showResult.bind(this)

    setSubmit(this.$form, {
      onBeforeSubmit() {
        console.log('Submitting form...')
      },
      onSuccess() {
        showResult()
      },
      onError(error) {
        console.error(error)
      }
    })
  }

  showResult() {
    this.$form.setAttribute('hidden', '')
    this.$hideOnSubmit.forEach(($elem) => $elem.setAttribute('hidden', ''))
    this.$showOnSubmit.forEach(($elem) => $elem.removeAttribute('hidden'))
  }
}

export const init = ($scope = document) => {
  const $elements = $scope.querySelectorAll(`[data-module="app-check-in"]`)

  return Array.from($elements).map(($element) => new CheckIn($element))
}
