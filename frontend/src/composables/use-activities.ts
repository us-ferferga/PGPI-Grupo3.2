import {Ref, ref} from 'vue';
import { useServer } from '@/composables';
import { Activity } from '@/api';

export const activities = ref <Activity[]>([]);
/**
 *
 */
export async function useActivities():Promise<Ref<Activity[]>> {
  const server = useServer();
  const activityResponse = await server.api.activity.activityList();

  activities.value = activityResponse.data;

  return activities;
}