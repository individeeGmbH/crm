<template>
  <Dialog v-model="show" :options="{ title: __('Post-Call Summary'), size: 'md' }">
    <template #body>
      <div class="px-4 pt-5 pb-6 sm:px-6 bg-surface-modal">
        <div class="flex items-center justify-between mb-5">
          <h3 class="text-2xl font-semibold leading-6 text-ink-gray-9">
            {{ __('Post-Call Summary') }}
          </h3>
          <Button variant="ghost" class="w-7" icon="x" @click="show = false"/>
        </div>

        <!-- Contact info -->
        <div v-if="data" class="flex items-center gap-3 mb-5 pb-4 border-b border-outline-gray-2">
          <Avatar
              :image="data.contact?.image"
              :label="data.contact?.full_name || data.phoneNumber || '?'"
              size="xl"
          />
          <div class="flex flex-col gap-1">
            <div class="font-medium text-ink-gray-9">
              {{ data.contact?.full_name || __('Unknown') }}
            </div>
            <div class="text-sm text-ink-gray-5">{{ data.phoneNumber }}</div>
            <Badge
                v-if="data.duration"
                :label="__('Duration: {0}', [data.duration])"
                theme="gray"
            />
          </div>
        </div>

        <!-- Summary textarea -->
        <div class="flex flex-col gap-1">
          <label class="block text-sm font-medium text-ink-gray-7">
            {{ __('Summary') }}
          </label>
          <FormControl
              type="textarea"
              v-model="summary"
              :placeholder="__('Enter a summary for this call...')"
              :rows="4"
          />
        </div>
        <ErrorMessage class="mt-3" :message="error"/>
      </div>
      <div class="flex flex-col gap-1">
        <label class="block text-sm font-medium text-ink-gray-7">
          {{ __('Rejection Reason') }}
        </label>
        <Link
            doctype="CRM Lost Reason"
            :value="rejectionReason"
            :placeholder="__('Select a reason...')"
            @change="(v) => (rejectionReason = v)"
        />
      </div>

      <div class="px-4 pt-4 pb-7 sm:px-6">
        <div class="flex justify-end gap-2">
          <Button :label="__('Skip')" @click="show = false"/>
          <Button
              variant="solid"
              :label="__('Save Summary')"
              :loading="loading"
              @click="saveSummary"
          />
        </div>
      </div>
    </template>
  </Dialog>
</template>

<script setup>
import {ref, watch} from 'vue'
import {Avatar, Badge, FormControl, ErrorMessage, call} from 'frappe-ui'

const props = defineProps({
  data: {type: Object, default: null},
})

const show = defineModel({type: Boolean})

const summary = ref('')
const rejectionReason = ref('')
const loading = ref(false)
const error = ref(null)

watch(show, (val) => {
  if (val) {
    summary.value = ''
    rejectionReason.value = ''
    error.value = null
  }
})

async function saveSummary() {
  if (!props.data?.name) {
    show.value = false
    return
  }
  loading.value = true
  error.value = null
  console.log(props.data.name)
  try {
    await call('frappe.client.set_value', {
      doctype: 'CRM Call Log',
      name: props.data.name,
      fieldname: {
        summary: summary.value,
        rejection_reason: rejectionReason.value,
      },
      value: summary.value,
    })
    show.value = false
  } catch (err) {
    error.value = err.messages?.[0] || err.message || __('Failed to save summary')
  } finally {
    loading.value = false
  }
}
</script>
